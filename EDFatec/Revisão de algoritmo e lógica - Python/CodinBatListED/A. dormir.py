#A. dormir
# dia_semana é True para dias na semana
# feriado é True nos feriados
# você pode ficar dormindo quando é feriado ou não é dia semana
# retorne True ou False conforme você vá dormir ou não
def dormir(dia_semana, feriado):
  '''if (dia == 'seg', 'ter', 'qua', 'qui', 'sex')
    dormir = False
  if (dia == 'sab', 'dom', 'feriadpo')
    dormir = True'''

  if feriado: return True
  if not dia_semana: return True
  return False
