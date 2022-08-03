.PHONY: freeze
freeze:
	pip freeze > requirements.txt

.PHONY: restore
restore:
	pip install -r requirements.txt

# This is not work because excuted another process.
.PHONY: activate
activate:
	. env/bin/activate

.PHONY: deactivate
deactivate:
	deactivate