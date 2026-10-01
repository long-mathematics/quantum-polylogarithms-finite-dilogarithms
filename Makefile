PYTHON ?= python3
LATEXMK ?= latexmk

.PHONY: all papers verify verify-exact clean
all: verify papers

papers:
	$(LATEXMK) -cd -pdf -interaction=nonstopmode -halt-on-error papers/quantum_polylogarithms.tex
	$(LATEXMK) -cd -pdf -interaction=nonstopmode -halt-on-error papers/finite_quantum_dilogarithms.tex

verify-exact:
	mkdir -p verification
	$(PYTHON) scripts/verify_rw_extensions.py > verification/finite_exact.txt
	$(PYTHON) scripts/checks_absolute.py --mode exact --output verification/quantum_exact.json

verify: verify-exact
	$(PYTHON) scripts/checks_absolute.py --mode numeric --output verification/quantum_numeric.json
	$(PYTHON) scripts/checks_v1.py --output verification/quantum_contours.json

clean:
	$(LATEXMK) -cd -c papers/quantum_polylogarithms.tex
	$(LATEXMK) -cd -c papers/finite_quantum_dilogarithms.tex
