// Valida data/catalogo.js conforme a seção 8.3 do projeto executivo.
// Uso: node scripts/validar-catalogo.mjs [caminho] [--estrito]
//   --estrito: miniatura inexistente vira ERRO (padrão: AVISO). OAD "em-construcao" pode usar o fallback.
import vm from 'node:vm';
import fs from 'node:fs';
import path from 'node:path';

const args = process.argv.slice(2);
const estrito = args.includes('--estrito');
const arquivo = args.find((a) => !a.startsWith('--')) ?? 'data/catalogo.js';
const raiz = path.resolve(path.dirname(arquivo), '..');

const ctx = { window: {} };
vm.createContext(ctx);
vm.runInContext(fs.readFileSync(arquivo, 'utf8'), ctx);
const { BTE_CATALOGO: C, BTE_META: M } = ctx.window;

const erros = [];
const avisos = [];
const cats = Object.keys(M.rotulos.categoria);
const fmts = Object.keys(M.rotulos.formato);
const sts = Object.keys(M.rotulos.status);
const acentos = ['navy', 'teal', 'orange'];
const recursos = ['simulador', 'laboratorio-virtual', 'fato-ou-fake', 'boss', 'badges', 'storytelling', 'painel', 'checklist', 'cornell-notes'];
const ids = new Set();
const ordens = new Set();
const cobertas = {};

for (const o of C) {
  const e = (m) => erros.push(`${o.id}: ${m}`);
  // 1. id
  if (!/^[a-z0-9-]+$/.test(o.id)) e('id fora do padrão (a-z, 0-9, hífen)');
  if (ids.has(o.id)) e('id duplicado');
  ids.add(o.id);
  if (!o.urlRepo.endsWith('/' + o.id)) e('urlRepo não termina com o id');
  // 2. textos
  if (o.titulo.length < 3 || o.titulo.length > 60) e('título fora de 3 a 60 caracteres');
  if (o.descricao.length > 140) e(`descricao com ${o.descricao.length} caracteres (máximo 140)`);
  if (!o.descricao.endsWith('.')) e('descricao deve terminar com ponto');
  if (o.tags.length < 1 || o.tags.length > 3) e('tags: de 1 a 3 itens');
  if (o.tags.some((t) => t.length > 24)) e('tag com mais de 24 caracteres');
  // 3. vocabulários
  if (!cats.includes(o.categoria)) e('categoria inválida');
  if (!fmts.includes(o.formato)) e('formato inválido');
  if (!sts.includes(o.status)) e('status inválido');
  if (!acentos.includes(o.acento)) e('acento inválido');
  if (o.recursos.some((r) => !recursos.includes(r))) e('recurso fora do vocabulário');
  // 4. status e URL
  if (o.status === 'publicado' && !(o.urlPages || '').startsWith(M.pagesBase)) e('publicado exige urlPages sob ' + M.pagesBase);
  if (o.status === 'em-construcao' && o.urlPages !== null) e('em-construcao exige urlPages null');
  // 5. lições e ordem
  if (o.licao.some((n) => !Number.isInteger(n) || n < 17 || n > 28)) e('licao deve ter inteiros de 17 a 28');
  if (ordens.has(o.ordem)) e('ordem duplicada');
  ordens.add(o.ordem);
  // 6. miniatura
  if (!o.miniaturaAlt) e('miniaturaAlt vazio');
  if (!fs.existsSync(path.join(raiz, o.miniatura))) {
    const msg = `miniatura ausente em disco: ${o.miniatura}`;
    if (estrito && o.status === 'publicado') e(msg); else avisos.push(`${o.id}: ${msg}`);
  }
  for (const n of o.licao) (cobertas[n] ||= []).push(o);
}

// 7. cobertura das lições 17 a 28
const soEmConstrucao = [];
let publicadas = 0;
for (let n = 17; n <= 28; n++) {
  if (!cobertas[n]) erros.push(`lição ${n} não é coberta por nenhum OAD`);
  else if (cobertas[n].some((o) => o.status === 'publicado')) publicadas++;
  else soEmConstrucao.push(n);
}

const comSimulador = C.filter((o) => o.recursos.some((r) => r === 'simulador' || r === 'laboratorio-virtual')).length;
console.log(`OAD: ${C.length} | lições publicadas: ${publicadas}/12 | só em construção: [${soEmConstrucao}] | OAD com simulador/lab: ${comSimulador}`);
console.log('maior descrição:', Math.max(...C.map((o) => o.descricao.length)), 'caracteres');
if (avisos.length) console.log('AVISOS:\n' + avisos.map((a) => '  ' + a).join('\n'));
console.log(erros.length ? 'ERROS:\n' + erros.map((x) => '  ' + x).join('\n') : 'Catálogo válido: 0 erros');
process.exit(erros.length ? 1 : 0);
