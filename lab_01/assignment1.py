def hello_name(name):
  return ("Hello "+name+"!")

def make_abba(a, b):
  return (a+b+b+a)

def make_tags(tag, word):
  return ("<"+tag+">"+word+"</"+tag+">")

def make_out_word(out, word):
  return (out[0]+out[1]+word+out[2]+out[3])

def extra_end(str):
  b = str[-2]+str[-1]
  return b+b+b 