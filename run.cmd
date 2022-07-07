:: Start Jupyter Lab
:jupyter
    ENDLOCAL & CALL conda run -p ./env jupyter lab --ip=0.0.0.0 --allow-root --no-browser --NotebookApp.token=""
    GOTO end

:: Run all tests in module
:test
	ENDLOCAL & CALL tox
	GOTO end

:: bingo out
:end
    EXIT /B