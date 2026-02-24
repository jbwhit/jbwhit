doc:
	uv run readme.py

update: doc
	git add .
	git commit -m "update profile"
	git push origin main
