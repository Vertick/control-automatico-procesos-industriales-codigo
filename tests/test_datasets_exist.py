"""Verifica el contrato de la carpeta data/.

El Lote 4 declaró que los datos sintéticos se generan in situ en cada
notebook con seed explícita. La carpeta `data/` queda como punto de
extensión documentado. Este test verifica la presencia de la estructura
y del README que documenta la política, no la presencia de ficheros
.csv (que no se incluyen en esta entrega).
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"


def test_data_root_exists():
    assert DATA.is_dir(), "data/ debe existir"


def test_data_subfolders_exist():
    assert (DATA / "synthetic").is_dir(), "data/synthetic/ debe existir"
    assert (DATA / "examples").is_dir(), "data/examples/ debe existir"


def test_data_readme_exists():
    assert (DATA / "README.md").is_file(), "data/README.md debe existir y documentar la política"


def test_seeds_explicit_in_reusable_notebooks():
    """Los notebooks reutilizables deben fijar seed explícita para reproducibilidad."""
    import json
    reusable = [
        ROOT / "python/cap03/C03_E02_ajuste_fopdt.ipynb",
        ROOT / "python/cap05/C05_E01_curve_fit_fopdt.ipynb",
        ROOT / "python/cap09/C09_E01_pid_antiwindup.ipynb",
        ROOT / "python/cap15/C15_E01_cusum_drift.ipynb",
        ROOT / "python/cap16/C16_E01_soft_sensor_pls.ipynb",
    ]
    for nb_path in reusable:
        with open(nb_path) as f:
            nb = json.load(f)
        text = "\n".join("".join(c.get("source", [])) for c in nb["cells"]
                         if c.get("cell_type") == "code")
        assert "np.random.seed" in text or "default_rng" in text, \
            f"sin seed explícita: {nb_path.name}"
