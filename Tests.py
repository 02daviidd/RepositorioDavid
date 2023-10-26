import torch

from Assignment1_ML.micalculadora import micalculadora as calc

# -------------------------------------------------
# Test case:
# -------------------------------------------------
tensor1 = torch.tensor([[1, 2], [3, 4]])
tensor2 = torch.tensor([[5, 6], [7, 8]])

print("Zeros Tensor:")
print(calc.tensor_ceros((2, 3)))
print("-------------------")

print("Ones Tensor:")
print(calc.tensor_unos((2, 3)))
print("-------------------")

print("Random Tensor:")
print(calc.tensor_random((2, 3)))
print("-------------------")

print("Sum of Tensors:")
print(calc.suma_tensors(tensor1, tensor2))
print("-------------------")

print("Product of Tensors:")
print(calc.multiplicar_tensors(tensor1, tensor2))
print("-------------------")

# Additional functions
tensor3 = torch.tensor([[1, 2], [3, 4], [5, 6], [7, 8]])
tensor4 = torch.tensor([1.5, 2.3, 3.8])

even_sum, odd_sum = calc.tensor_par_impar(tensor3)
print("Even Sum:")
print(even_sum)
print("Odd Sum:")
print(odd_sum)
print("-------------------")

print("Reversed Tensor:")
reversed_tensor = calc.invertir_tensor(tensor3)
print(reversed_tensor)
print("-------------------")

print("Rounded Tensor:")
rounded = calc.redondear(tensor4)
print(rounded)
print("-------------------")