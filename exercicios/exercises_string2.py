#!/usr/bin/python -tt
# coding: utf-8
import unittest

# Dado uma string, se o seu comprimento for pelo menos 3, adicione 'ing' ao final.
# Caso já termine em 'ing' adicionar "ly".
# Se o comprimento da string for inferior a 3, deixe-o inalterado.
# Retorne a string resultante.
def verbing(s):
    if "ing" in s:
      return s + "ly"
    elif len(s) >= 3:
      return s + "ing"
    else:
      return s

# (google solution)
def verbingV2(s):
    if len(s) > 3:
      if s.endswith("ing"):
        return s + "ly"
      else:
        return s + "ing"
    return s

# Dado um astring, procurar a primeira ocorrência da substring 'not' e 'bad'
# Se 'bad' vier após o 'not'
# substituir todo o trecho "not ... bad" por 'good'
# Retorne a string resultante.
def not_bad(s):
    n = s.find('not')
    b = s.find('bad')
    if n != -1 and b != -1 and b > n:
      s = s[:n] + 'good' + s[b+3:]
    return s
# Considere dividir uma string em duas metades.
# Se o comprimento for par, a parte da frete (front) e a parte de trás (back) são do mesmo tamanho.
# Se o comprimento for ímpar, o caracter extra irá para a aprte da frente.
#
# Dado 2 strings, 'a' e 'b', retornar um string na forma
# a front + b front + a back + b back
def front_back(a, b):
    pass

class MyTest(unittest.TestCase):

  def test_verbing(self):
    self.assertEqual(verbing('hail'), 'hailing')
    self.assertEqual(verbing('swiming'), 'swimingly')
    self.assertEqual(verbing('do'), 'do')

  def test_not_bad(self):
    self.assertEqual(not_bad('This movie is not so bad'), 'This movie is good')
    self.assertEqual(not_bad('This dinner is not that bad!'), 'This dinner is good!')
    self.assertEqual(not_bad('This tea is not hot'), 'This tea is not hot')
    self.assertEqual(not_bad("It's bad yet not"), "It's bad yet not")

  def test_front_back(self):
    self.assertEqual(front_back('abcd', 'xy'), 'abxcdy')
    self.assertEqual(front_back('abcde', 'xyz'), 'abcxydez')
    self.assertEqual(front_back('Kitten', 'Donut'), 'KitDontenut')

if __name__ == '__main__':
  unittest.main()