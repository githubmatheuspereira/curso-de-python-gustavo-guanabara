celsius = float(input('Qual a temperatura em celsius? '))
fahrenheit = float((9 * celsius) / 5) + 32
print ('A temperatura em celsius é \033[0;32m{}°C\033[m e em Fahrenheit ficará \033[0;35m{}°F\033[m'.format(celsius, fahrenheit))
