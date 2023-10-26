#Name: David Sanz Mínguez

# PyTorch Tensor Operations
This Python module provides a collection of functions for performing various operations 
on PyTorch 2-dimensional tensors. 
It includes functions for creating tensors filled with zeros, ones, and random values, 
as well as functions for tensor addition and multiplication. 
Additionally, there are some creative functions for manipulating tensors.

#Functions
**tensor_ceros(shape):** Returns a tensor filled with zeros of the specified shape.
**tensor_unos(shape):** Returns a tensor filled with ones of the specified shape.
**tensor_random(shape):** Returns a tensor filled with random values of the specified shape.
**suma_tensors(tensor1, tensor2):** Returns the sum of two tensors.
**multiplicar_tensors(tensor1, tensor2):** Returns the element-wise multiplication of two tensors.

#Additional functions
**tensor_par_impar(tensor):** Divides the rows of a tensor into even and odd rows and calculates the sums separately.
**invertir_tensor(tensor):** Reverses the order of rows in a 2D tensor.
**redondear(tensor):** Rounds the values in a tensor to the nearest integer.

#Tests
At the end of the **Tests.py**, you will find a set of test cases that can be used to verify
the functionality of the provided functions in this module. 
Be sure to run these test cases to ensure that the functions work as expected.

#Steps for installation
Para instalar la librería, utilice el siguiente comando:
```bash
pip install -U git+https://github.com/02daviidd/RepositorioDavid
