import sys
sys.path.append("..")
from common import io
import attribute

def generate_inputs(shape, len):
  ret = list()
  for i in range(len):
    ret.append(attribute.CastRandomInput(shape))
  return ret

if __name__ == "__main__":
  inputs = generate_inputs([1024, 1024], 20)
  path = "inputs.pkl"
  io.Pickle.save(inputs, path)
