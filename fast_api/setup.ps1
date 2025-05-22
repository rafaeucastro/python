# Define o nome do ambiente virtual
$venvName = "venv"

Write-Host "Criando ambiente virtual..."
python -m venv $venvName

Write-Host "Ativando ambiente virtual..."
& ".\$venvName\Scripts\Activate.ps1"

Write-Host "Atualizando pip..."
python -m pip install --upgrade pip

Write-Host "Instalando pacotes necessários..."
pip install -r requirements.txt

Write-Host "Instalação concluída!"