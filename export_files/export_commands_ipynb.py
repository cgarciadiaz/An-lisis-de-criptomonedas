# Ir a la ruta
cd C:\Users\cgarcia\AnacondaProjects\cryptocurrency_analysis

# Comandos para exportar
# jupyter nbconvert --to html nombre_del_archivo
# jupyter nbconvert --to pdf nombre_del_archivo   
# jupyter nbconvert --to latex --post PDF nombre_del_archivo
jupyter nbconvert --to html *.ipynb
move *.html C:\Users\cgarcia\AnacondaProjects\cryptocurrency_analysis\export_files
    
jupyter nbconvert --to html cryptocurrency_analysis.ipynb
jupyter nbconvert --to html cryptocurrency_indicators.ipynb
jupyter nbconvert --to html cryptocurrency_prediction_deep_learning.ipynb
jupyter nbconvert --to html cryptocurrency_prophet.ipynb
jupyter nbconvert --to html cryptocurrency_regression.ipynb

# Mover los archivos a la carpeta export
move cryptocurrency_analysis.html C:\Users\cgarcia\AnacondaProjects\cryptocurrency_analysis\export
move cryptocurrency_indicators.html C:\Users\cgarcia\AnacondaProjects\cryptocurrency_analysis\export
move  cryptocurrency_prediction_deep_learning.html C:\Users\cgarcia\AnacondaProjects\cryptocurrency_analysis\export
move  cryptocurrency_regression.html C:\Users\cgarcia\AnacondaProjects\cryptocurrency_analysis\export
move  cryptocurrency_prophet.html C:\Users\cgarcia\AnacondaProjects\cryptocurrency_analysis\export