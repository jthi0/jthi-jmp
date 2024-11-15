import base64
import io
import jmp
import numpy as np
import pandas as pd
import shap
import xgboost

import matplotlib.pyplot as plt

#print(X.head(), X.columns.values)

# Get example data
X, y = shap.datasets.california()
print(X.head, X.columns.values)

# Create a model
model = xgboost.XGBRegressor().fit(X, y)

# explain the model's predictions using SHAP
explainer = shap.TreeExplainer(model)
shap_values = explainer(X)


# visualize the first prediction's explanation
fig = plt.figure()
#shap.plots.waterfall(shap_values[0], show=False)
shap.plots.beeswarm(shap_values, show=False)
# shap.summary_plot(shap_values, show=False)
# shap.summary_plot(shap_values, show=False, plot_type='violin')
# shap.plots.bar(shap_values[0]) # explain single row
# shap.plots.waterfall(shap_values[0])

#shap.plots.force(shap_test)
#plt.savefig(f'my_plot.png', bbox_inches='tight')

my_iobytes = io.BytesIO()
plt.savefig(my_iobytes, format='jpg', bbox_inches='tight')
my_iobytes.seek(0)
base64data = base64.b64encode(my_iobytes.read()).decode()
print(base64data)
jmp.run_jsl('''
img = New Image(Char To Blob(Python Get(base64data), "base64"));
New Window("test", img);
'''
)

df = pd.DataFrame(
    np.c_[shap_values.base_values, shap_values.values],
    columns = ["bv"] + list(X.columns)
)
# add response to dataframe
df = pd.concat([df, pd.DataFrame(y, columns=["Values"])], axis=1)

# convert pandas dataframe to JMP data table for visualization purposes
dt2 = jmp.DataTable('BC2',df.shape[0])
for j in range(df.shape[1]):
	dt2.new_column(df.columns[j], jmp.DataType.Numeric, jmp.ModelingType.Continuous)
	dt2[j] = list(df.iloc[:,j])