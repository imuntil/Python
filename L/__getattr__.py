class Chain():
  def __init__(self, path=''):
    self._path = path
  def __getattr__(self, path):
    return Chain('{}/{}'.format(self._path, path))
  def __str__(self):
    return self._path
  __repr__ = __str__
  def __call__(self):
    print('lala')


c = Chain('xx')
print(c.status.user.timeline.list)
c()