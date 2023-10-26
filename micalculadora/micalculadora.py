import torch
# -------------------------------------------------
# Zero, ones, random, sum and multiply functions:
# -------------------------------------------------
def tensor_ceros(shape):
    return torch.zeros(shape)


def tensor_unos(shape):
    return torch.ones(shape)


def tensor_random(shape):
    return torch.rand(shape)


def suma_tensors(tensor1, tensor2):
    if tensor1.size() != tensor2.size():
        raise ValueError("Tensors must have the same size for addition.")
    return tensor1 + tensor2


def multiplicar_tensors(tensor1, tensor2):
    if tensor1.size() != tensor2.size():
        raise ValueError("Tensors must have the same size for multiplication.")
    return torch.mul(tensor1, tensor2)


# -------------------------------------------------
# Additional functions to manipulate tensors:
# -------------------------------------------------
def tensor_par_impar(tensor):
    """
        Take a tensor and split its rows into two groups: even rows and odd rows.
        Then, calculate the sum of even rows and odd rows separately, and
        return two tensors with the results.
    :param tensor:
    :return: two tensors
    """
    if tensor.size(0) % 2 != 0:
        raise ValueError("Tensor must have an even number of rows.")

    even_sum = torch.sum(tensor[::2, :], dim=0)
    odd_sum = torch.sum(tensor[1::2, :], dim=0)

    return even_sum, odd_sum


def invertir_tensor(tensor):
    """
    Take a 2D tensor and reverse the order of its rows
    :param tensor:
    :return: tensor
    """
    if len(tensor.size()) != 2:
        raise ValueError("Tensor must be 2D for row reversal.")

    tensor_invertido = torch.flip(tensor, [0])
    return tensor_invertido


def redondear(tensor):
    """
    If the tensor contains decimal values, it returns the tensor rounded to the nearest integer.
    """
    redondeado = torch.round(tensor)
    return redondeado



