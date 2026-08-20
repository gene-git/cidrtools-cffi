# docs/Makefile
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = .
BUILDDIR      = _build
PKG           = cidrtools-cffi

SOURCES = conf.py index.rst py-api.rst Readme.rst ../../version.txt \
          $(wildcard ../../cidrtools/*.py) 

.PHONY: help Makefile clean
html: $(BUILDDIR)/html/index.html
latexpdf: $(PKG).pdf

help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# The real file target that tracks dependencies
$(BUILDDIR)/html/index.html: $(SOURCES)
	@$(SPHINXBUILD) -b html "$(SOURCEDIR)" "$(BUILDDIR)/html" $(SPHINXOPTS) $(O)
	@echo "HTML doc build complete. Path: $@"

# The real file target that tracks dependencies
$(PKG).pdf: $(SOURCES)
	@$(SPHINXBUILD) -b latex "$(SOURCEDIR)" "$(BUILDDIR)/latex" $(SPHINXOPTS) $(O)
	@echo "Running xelatex compiler framework..."
	$(MAKE) -C "$(BUILDDIR)/latex" all-pdf LATEXOPTS="-interaction=nonstopmode"
	$(MAKE) -C "$(BUILDDIR)/latex" all-pdf LATEXOPTS="-interaction=nonstopmode"
	@rsync -av $(BUILDDIR)/latex/$(PKG).pdf .
	@touch $(PKG).pdf
	@echo "PDF doc build complete. Path: $@"

clean:
	rm -rf $(BUILDDIR)
	rm -f $(PKG).pdf

