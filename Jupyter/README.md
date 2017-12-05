# Jupyter

Directory for Jupyter related wokflows.

## Jupyter installation - system wide

Along this project Python uses virtual env. To replicate and run code one can
use Jupyter links for `.ipynb` files or try to replicate the virtual env from
the following way:

1. Upgrade pip for python3: `pip3 install --upgrade pip`
2. Install Jupyter: `pip3 install jupyter` 
     
#### Run Jupyter using VirtualEnv

1. Install Python3 virtual env [See README](../README.md)
2. Inside VE we need to install ipython kernel for Jupyter: `pip install 
ipykernel` (`pip` should be equivalent `pip3`)
    * test:
     
    ```
    (myVEdir)$ pip freeze --local | grep kernel
    ipykernel==4.6.1
    ```
    
3. One can install jupyter inside VE or system-wide. 
 
    * system wide (**recommended**): `$ pip3 install jupyter`
    * within VE (this will allow to run Jupyter **ONLY** based on files 
    within `myVEdir` so you `.ipynb` would have 
    to be also in the `myVEdir`):
    * check outdated local packages (and new versions):  `pip list --outdated
     --local`
    * update local packages that are outdated:
`pip list --outdated --local --format=freeze | cut -d '=' -f 1 | xargs -0 -I {} -n1 pip install -U {}`

Then install `ipykernel` inside VE so that Jupyter can use it:     
`(myVEdir)$ python -m  ipykernel install --user --name=myVEdir`

    
4. Regardless if running as VE or system-side: to run Jupyter server just 
issue:  `jupyter notebook` in directory when you want it to start the Jupyter
browser.

5. Now, in Jupyter web interface you can click `Kernel -> Change kernel` and 
you VE name should be there visible.
    * test:
    
6. Embed Jupyter Widget in HTML
http://ipywidgets.readthedocs.io/en/stable/embedding.html

Installation: http://ipywidgets.readthedocs.io/en/stable/user_install.html
and then:
`jupyter nbextension install --py widgetsnbextension --user`
and
`jupyter nbextension enable widgetsnbextension --user --py`
    
[tutorial on widgets](http://nbviewer.jupyter.org/github/quantopian/ipython/blob/master/examples/Interactive%20Widgets/Index.ipynb)



---
###### LICENSING
Code: AGPL-3.0 Content:
[![CC-by-SA-4.0](https://licensebuttons.net/l/by-sa/4.0/88x31.png)](https://creativecommons.org/licenses/by-sa/4.0/)
