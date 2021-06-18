

### To create the singularity image yourself

The definition file contains more than tempo2, libstempo and psrchive for python3. It also install tensorflow and keras (for deep learning purpose). Feel free to remove these parts if you want something lighter and you have no use of deep learning. To create the singularity image, run this command:

```
singularity build nameofyourimg psrchive3.def
```

Your image can either be: 

- a *.sif image -> you cannot modify it after the creation

- a */ image -> this is a sandbox folder, you can modify it whenever you want

To run the image you can use :

```
singularity shell -w nameofyourimg/
```

You will be able to install new soft and modify environment variable as you wish but it will apply only for you nameofyourimg/ image. 

  

