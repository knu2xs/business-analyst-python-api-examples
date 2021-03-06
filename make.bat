:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:: LICENSING                                                                    :
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::
:: Copyright 2020 Esri
::
:: Licensed under the Apache License, Version 2.0 (the "License"); You
:: may not use this file except in compliance with the License. You may
:: obtain a copy of the License at
::
:: http://www.apache.org/licenses/LICENSE-2.0
::
:: Unless required by applicable law or agreed to in writing, software
:: distributed under the License is distributed on an "AS IS" BASIS,
:: WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
:: implied. See the License for the specific language governing
:: permissions and limitations under the License.
::
:: A copy of the license is available in the repository's
:: LICENSE file.

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:: VARIABLES                                                                    :
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

SETLOCAL
SET PROJECT_DIR=%cd%
SET PROJECT_NAME=business-analyst-python-api-examples


:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:: COMMANDS                                                                     :
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:: Jump to command
GOTO %1

:: Perform data preprocessing steps contained in the make_data.py script.
:data
    ENDLOCAL & (
        CALL src/make_data.py
        ECHO ^>^>^> Data setup complete.
    )
    GOTO end

:: Make documentation using Sphinx!
:docs
    ENDLOCAL & (
        CALL conda run -p "%PROJECT_DIR%\env" sphinx-build -a -b html docsrc docs
    )
	GOTO end

:: Create the Reveal.js slides from all the notebooks
:slides
    ENDLOCAL & CAll conda run - ./env python src/ck_tools/create_reveal_slides.py
    GOTO end

:: Build the local environment from the environment file
:env
    ENDLOCAL & (
        
        :: Create new environment by cloning the original
        CALL conda create -p "%PROJECT_DIR%\env" --clone "C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3"

        :: Add more fun stuff from environment file
        CALL conda env update -p "%PROJECT_DIR%\env" -f environment.yml

        :: Install the local package in development (experimental) mode
        CALL conda run -p "%PROJECT_DIR%\env" python -m pip install -e .

        :: Activate the environment so you can get to work
        CALL activate "%PROJECT_DIR%\env"

    )
    GOTO end

:: Start Jupyter Lab
:jupyter
    ENDLOCAL & CALL conda run -p "%PROJECT_DIR%\env" jupyter lab --ip=0.0.0.0 --allow-root --no-browser --NotebookApp.token=""
    GOTO end

:: Run all tests in module
:test
	ENDLOCAL & CALL tox
	GOTO end

:end
    EXIT /B
