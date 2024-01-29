cd test_results
cat log.raw | tfs report coverage > coverage.md
cat log.raw | tfs report results > results.md
cat coverage.md | tfs document convert > coverage.html
cat results.md | tfs document convert > results.html
