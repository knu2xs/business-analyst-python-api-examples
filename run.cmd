:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:: LICENSING                                                                    :
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::
:: Copyright 2020 Joel McCune
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

SETLOCAL

:: Jump to command
GOTO %1

:: Start Jupyter Lab
:jupyter
    ENDLOCAL & CALL conda activate ./env && jupyter lab --ip=0.0.0.0 --allow-root --no-browser --NotebookApp.token=""
    GOTO end

:: start Jupyter Lab for the arcgis-python-api samples
:jupyter-guide
    ENDLOCAL & CALL conda activate ./env && jupyter lab --ip=0.0.0.0 --allow-root --no-browser --NotebookApp.token="" --notebook-dir="../arcgis-python-api/guide"
    GOTO end

:: start Jupyter Lab for the arcgis-python-api samples
:jupyter-samples
    ENDLOCAL & CALL conda activate ./env && jupyter lab --ip=0.0.0.0 --allow-root --no-browser --NotebookApp.token="" --notebook-dir="../arcgis-python-api/samples"
    GOTO end

:end
    EXIT /B
