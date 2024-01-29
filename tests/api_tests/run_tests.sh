rm -r test_results || true
mkdir test_results
python3 regression.py --log test_results/log.raw
