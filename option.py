class Option(object):
  def __init__(self):
    pass
    
  def __new__(self, val):
    if val is None:
      return Nothing()
    else:
      return Some(val)

  def __iter__(self):
      self.current = 0
      return self

  def next(self):
      if self.current > 0:
          raise StopIteration
      else:
          self.current += 1
          return self.val
            
class Some(Option):
  def __new__(*args, **kw):
    return object.__new__(Some)
  
  def __init__(self, val):
    self.val = val

  def isEmpty(self):
    return False
    
  def isDefined(self):
    return True
  
  def map(self, f):
    return self.__class__(f(self.val))
  
  def flatMap(self, f):
    ret = f(self.val)
    if not isinstance(ret, Option):
      raise Exception("f must return an Option.")
    return ret
  
  def filter(self, f):
    if f(self.val):
      return self
    else:
      return Nothing()
    
  def foreach(self, f):
    f(self.val)
  
  def get(self):
    return self.val
    
  def getOrElse(self, d):
    return self.val
  
def singleton(D):
    class C(D):
      _instance = None
      def __new__(cls, *args, **kwargs):
        if not cls._instance:
          cls._instance = D.__new__(cls, *args, **kwargs)
        return cls._instance
    C.__name__ = D.__name__
    return C

@singleton
class Nothing(Option):
  def __new__(*args, **kw):
    return object.__new__(Nothing)

  def __init__(self, *args, **kw):
    pass
    
  def next(self):
    raise StopIteration
  
  def isEmpty(self):
    return True
    
  def isDefined(self):
    return False
  
  def map(self, f):
    return self
  
  def flatMap(self, f):
    return self
  
  def filter(self, f):
    return self
    
  def foreach(self, f):
    pass
  
  def get(self):
    raise Exception("No such element.")
    
  def getOrElse(self, d):
    return d