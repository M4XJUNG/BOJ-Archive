# 28290 안밖? 밖안? 계단? 역계단?
memo = input()
if memo == 'fdsajkl;' or memo == 'jkl;fdsa': 
  print('in-out')
elif memo == 'asdf;lkj' or memo == ';lkjasdf':
  print('out-in')
elif memo == 'asdfjkl;':
  print('stairs')
elif memo == ';lkjfdsa':
  print('reverse')
else: print('molu')