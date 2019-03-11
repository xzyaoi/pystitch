package:
		python3 setup.py sdist bdist_wheel

publish-test:
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

publish-prod:
	twine upload dist/*

clean:
	rm -rf build
	rm -rf dist
	rm -rf pystitch.egg-info
