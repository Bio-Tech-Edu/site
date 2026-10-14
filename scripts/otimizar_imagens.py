#!/usr/bin/env python3
"""Gera logotipos, ícones e imagem de compartilhamento do portal Bio+Tech EduDesign.

Entradas (nunca alteradas), em --origem (padrão: assets/logo/origem):
  favicon.png  logotipo circular, RGBA (esperado 600x600)
  hero.png     banner (esperado 1667x584)

Saídas, em --saida (padrão: assets/logo):
  biotech-logo.webp, icon-192.png, icon-512.png, apple-touch-icon.png,
  favicon.ico (16, 32 e 48) e og-image.jpg (1200x630, até 200 KB).

Requisitos: Python 3 + Pillow (sem outras dependências).
O script é idempotente: sempre regenera tudo a partir dos originais.
Uso: python3 scripts/otimizar_imagens.py [--origem PASTA] [--saida PASTA]
"""
import argparse
import io
import sys
from pathlib import Path

try:
    from PIL import Image, features
except ImportError:
    sys.exit("Erro: o Pillow não está instalado. Rode: pip install pillow")

LANCZOS = Image.Resampling.LANCZOS
AMPLIACAO_MAXIMA = 1.1          # nenhuma imagem pode ser ampliada além disso
OG_LARGURA, OG_ALTURA = 1200, 630
OG_BORDA = 4                    # px removidos de cada borda do hero.png
OG_LIMITE_KB = 200
OG_QUALIDADE_INICIAL = 82
OG_QUALIDADE_MINIMA = 40


class ErroImagem(Exception):
    """Erro esperado, com mensagem clara em português."""


def abrir(caminho: Path) -> Image.Image:
    if not caminho.is_file():
        raise ErroImagem(
            f"Arquivo original não encontrado: {caminho}\n"
            "       Copie favicon.png e hero.png para a pasta de origem "
            "(padrão: assets/logo/origem) ou use --origem."
        )
    try:
        img = Image.open(caminho)
        img.load()
        return img
    except Exception as exc:  # imagem corrompida ou formato inesperado
        raise ErroImagem(f"Não foi possível abrir {caminho}: {exc}")


def checar_ampliacao(nome: str, origem_px: int, destino_px: int) -> None:
    fator = destino_px / origem_px
    if fator > AMPLIACAO_MAXIMA:
        raise ErroImagem(
            f"{nome}: a origem tem {origem_px} px e o destino {destino_px} px "
            f"(ampliação de {fator:.2f}x, máximo {AMPLIACAO_MAXIMA}x). "
            "Use um original maior."
        )


def redimensionar(img: Image.Image, lado: int) -> Image.Image:
    return img.resize((lado, lado), LANCZOS)


def gerar_logotipos(origem: Path, saida: Path) -> None:
    logo = abrir(origem / "favicon.png").convert("RGBA")
    largura, altura = logo.size
    if largura != altura:
        raise ErroImagem(f"favicon.png deve ser quadrado (veio {largura}x{altura}).")
    lado = largura
    for nome, destino in (("biotech-logo.webp", 512), ("icon-192.png", 192),
                          ("icon-512.png", 512), ("apple-touch-icon.png", 150),
                          ("favicon.ico", 48)):
        checar_ampliacao(nome, lado, destino)

    # WebP com transparência
    redimensionar(logo, 512).save(saida / "biotech-logo.webp", "WEBP",
                                  quality=90, method=6)
    # PNGs com transparência
    redimensionar(logo, 192).save(saida / "icon-192.png", "PNG", optimize=True)
    redimensionar(logo, 512).save(saida / "icon-512.png", "PNG", optimize=True)

    # apple-touch-icon: 180x180, fundo branco opaco, logotipo de 150x150 centralizado
    miolo = redimensionar(logo, 150)
    fundo = Image.new("RGB", (180, 180), (255, 255, 255))
    fundo.paste(miolo, (15, 15), miolo.getchannel("A"))
    fundo.save(saida / "apple-touch-icon.png", "PNG", optimize=True)

    # favicon.ico com 16, 32 e 48 (cada tamanho reduzido com LANCZOS a partir do original)
    tamanhos = [16, 32, 48]
    versoes = [redimensionar(logo, t) for t in tamanhos]
    versoes[-1].save(saida / "favicon.ico", format="ICO",
                     sizes=[(t, t) for t in tamanhos],
                     append_images=versoes[:-1])


def gerar_og(origem: Path, saida: Path) -> str:
    hero = abrir(origem / "hero.png")
    if hero.mode in ("RGBA", "LA", "P"):
        hero = hero.convert("RGBA")
        base = Image.new("RGBA", hero.size, (255, 255, 255, 255))
        hero = Image.alpha_composite(base, hero)
    hero = hero.convert("RGB")
    largura, altura = hero.size

    # 1) remove a borda arredondada (4 px de cada lado)
    util = hero.crop((OG_BORDA, OG_BORDA, largura - OG_BORDA, altura - OG_BORDA))
    larg_u, alt_u = util.size

    # 2) recorte central na proporção 1200:630
    alvo = OG_LARGURA / OG_ALTURA
    if larg_u / alt_u >= alvo:                 # mais largo: corta dos lados
        larg_c, alt_c = round(alt_u * alvo), alt_u
    else:                                      # mais alto: corta em cima e embaixo
        larg_c, alt_c = larg_u, round(larg_u / alvo)
    esq, topo = (larg_u - larg_c) // 2, (alt_u - alt_c) // 2
    recorte = util.crop((esq, topo, esq + larg_c, topo + alt_c))
    checar_ampliacao("og-image.jpg", larg_c, OG_LARGURA)

    # 3) redimensiona e salva; reduz a qualidade de 2 em 2 até caber em 200 KB
    final = recorte.resize((OG_LARGURA, OG_ALTURA), LANCZOS)
    qualidade = OG_QUALIDADE_INICIAL
    while True:
        buf = io.BytesIO()
        final.save(buf, "JPEG", quality=qualidade, progressive=True, optimize=True)
        if buf.tell() <= OG_LIMITE_KB * 1024:
            break
        qualidade -= 2
        if qualidade < OG_QUALIDADE_MINIMA:
            raise ErroImagem(f"og-image.jpg não coube em {OG_LIMITE_KB} KB "
                             f"nem com qualidade {OG_QUALIDADE_MINIMA}.")
    (saida / "og-image.jpg").write_bytes(buf.getvalue())
    return (f"recorte {larg_c}x{alt_c} a partir de {largura}x{altura} "
            f"(sem {OG_BORDA} px por borda), qualidade JPEG {qualidade}")


def relatorio(saida: Path) -> bool:
    """Lê de volta cada arquivo gerado, imprime a tabela e confere os critérios."""
    nomes = ["biotech-logo.webp", "icon-192.png", "icon-512.png",
             "apple-touch-icon.png", "favicon.ico", "og-image.jpg"]
    linhas, info = [], {}
    for nome in nomes:
        caminho = saida / nome
        kb = caminho.stat().st_size / 1024
        with Image.open(caminho) as img:
            if nome == "favicon.ico":
                tams = sorted(img.info.get("sizes", {img.size}))
                dim = ", ".join(f"{w}x{h}" for w, h in tams)
            else:
                tams, dim = [img.size], f"{img.size[0]}x{img.size[1]}"
            info[nome] = (tams, img.mode, kb)
        linhas.append((nome, dim, info[nome][1], f"{kb:.1f}"))

    cab = ("arquivo", "dimensões", "modo", "KB")
    larg = [max(len(str(l[i])) for l in linhas + [cab]) for i in range(4)]
    fmt = " | ".join("{:<%d}" % w for w in larg)
    print(fmt.format(*cab))
    print("-+-".join("-" * w for w in larg))
    for l in linhas:
        print(fmt.format(*l))

    checks = [
        ("og-image.jpg com 1200x630", info["og-image.jpg"][0] == [(1200, 630)]),
        (f"og-image.jpg com no máximo {OG_LIMITE_KB} KB", info["og-image.jpg"][2] <= OG_LIMITE_KB),
        ("biotech-logo.webp em RGBA", info["biotech-logo.webp"][1] == "RGBA"),
        ("icon-192.png em RGBA", info["icon-192.png"][1] == "RGBA"),
        ("icon-512.png em RGBA", info["icon-512.png"][1] == "RGBA"),
        ("apple-touch-icon.png 180x180 opaco (RGB)",
         info["apple-touch-icon.png"][0] == [(180, 180)] and info["apple-touch-icon.png"][1] == "RGB"),
        ("favicon.ico com os tamanhos 16, 32 e 48",
         sorted(info["favicon.ico"][0]) == [(16, 16), (32, 32), (48, 48)]),
    ]
    print("\nConferência:")
    for texto, ok in checks:
        print(f"  [{'ok' if ok else 'FALHA'}] {texto}")
    return all(ok for _, ok in checks)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--origem", default="assets/logo/origem", help="pasta com favicon.png e hero.png")
    ap.add_argument("--saida", default="assets/logo", help="pasta de destino dos arquivos gerados")
    args = ap.parse_args()
    origem, saida = Path(args.origem), Path(args.saida)

    try:
        if not features.check("webp"):
            raise ErroImagem("Este Pillow não tem suporte a WebP. Atualize: pip install -U pillow")
        if origem.resolve() == saida.resolve():
            raise ErroImagem("--origem e --saida não podem ser a mesma pasta (os originais não são alterados).")
        saida.mkdir(parents=True, exist_ok=True)
        gerar_logotipos(origem, saida)
        detalhe = gerar_og(origem, saida)
    except ErroImagem as exc:
        print(f"Erro: {exc}", file=sys.stderr)
        return 1

    print(f"Origem: {origem} | Saída: {saida}")
    print(f"og-image.jpg: {detalhe}\n")
    return 0 if relatorio(saida) else 1


if __name__ == "__main__":
    sys.exit(main())
