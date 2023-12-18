# Aneel_tariffs
Este código é uma consulta pública na Aneel que verifica se foram publicadas novas tarifas de distribuidoras.
Caso alguma tarifa nova seja encontrada, ela é salva no banco de dados e envia um email para notificar que econtrou uma nova tarifa.

O código utilizia um sistema de cache de 24 horas, o job é rodado no inicio da manha, e preenche o cache, todas as consultas após o cache preenchidas são realizadas no próprio cache para evitar sobreecarregamento.

O programa também mantém o maior id no banco de dados no arquivo max_id para evitar consultar o banco antes de buscar novas tarifas, dessa forma otimiza tempo.

NECESSÁRIO ########
pip install pandas
pip install openpyxl
