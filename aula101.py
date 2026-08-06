# try, except, else e finaly

# a = 10
# b = 0
# c = a / b

try:
  a = 10
  b = 0
  #print(b[0])
  #print('Linha1'[1000])
  
  c = a / b
  print('linha2')

except ZeroDivisionError as e:
  print(e.__class__.__name__)
  print(e)
except NameError:
  print('Nome b não está definido.')
except (TypeError, IndexError) as error:
  print('TypeError + IndexError.')
  print('MSG', error)
  print('Nome:', error.__class__.__name__)
except Exception:
  print('ERRO DESCONHECIDO.')  

print('CONTINUAR')


print()
print()