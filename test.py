from mock import Mock
import sys
import types
import unittest


def side_effect(*args, **kwargs):
  return responses.pop(0)


module_name = 'hackerforms'
bogus_module = types.ModuleType(module_name)
sys.modules[module_name] = bogus_module
bogus_module.read_number = Mock(name=module_name+'.read_number', side_effect = side_effect)
bogus_module.read_dropdown = Mock(name=module_name+'.read_dropdown', side_effect = side_effect)
bogus_module.display = Mock(name=module_name+'.display', side_effect = lambda *args, **kwargs: print(*args, **kwargs))



class TestBar(unittest.TestCase):
    def test_bar(self):
      global responses
      responses = [1,2, "Test answer"]
      import script
      self.assertEquals(script.sum, 3)
      self.assertEquals(script.ans, "Test answer")
        
        
if __name__ == "__main__":
  unittest.main()