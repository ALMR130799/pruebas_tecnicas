import pandas as pd

# DataFrame de ejemplo para empleados
empleados = pd.DataFrame({
    'empleado_id': [1, 2, 3, 4, 5,6],
    'nombre': ['Juan', 'María', 'Pedro', 'Luis', 'Alberto','Tomás'],
    'departamento_id': [101, 102, 101, 103,104,105]
})

# DataFrame de ejemplo para departamentos
departamentos = pd.DataFrame({
    'departamento_id': [101, 102, 103, 104],
    'nombre': ['Ventas', 'Marketing', 'Tecnología', 'Recursos Humanos']
})


resultado_inner = pd.merge(empleados, departamentos, on='departamento_id', how='inner')
print("INNER JOIN:")
print(resultado_inner)

# Realizar un LEFT JOIN entre los DataFrames empleados y departamentos
resultado_left = pd.merge(empleados, departamentos, on='departamento_id', how='left')
print("\nLEFT JOIN:")
print(resultado_left)

resultado_left = pd.merge(empleados, departamentos, on='departamento_id', how='right')
print("\nRIGHT JOIN:")
print(resultado_left)

