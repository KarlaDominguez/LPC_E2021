[int]$valor1 = Read-Host "valor 1"
[int]$valor2 = Read-Host "valor 2"

Function Get-Suma {
param(
$N1, $N2
)

$Resultado = $N1 + $N2
Write-host 'Resultado de la suma' $Resultado
}

Get-Suma -N1 $valor1 -N2 $valor2
if ( $valor1 -match $valor2 ){
    echo ''
    Write-host "valor1 y valor2 son los mismos "
}
echo ''
echo 'Tabla de multiplicar del primer valor, del 1 al 10'
$val=0
while($val -ne 10)
{
    $val++
    $x =($val*$valor1)
    Write-host $valor1 '*' $val' = '$x
  
}