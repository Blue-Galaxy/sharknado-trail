class Graph:
  """Representation of a simple graph using an adjacency map"""
  def __init__(self, directed = False):
    """Create an empty Graph
       Undirected by default"""
    self._outgoing = {}
    self._incoming = {} if directed else self._outgoing


  def is_directed(self):
    return self._incoming is not self._outgoing


  def vertex_count(self):
    """return the number of vertices int he graph"""
    return len(self._outgoing)


  def vertices(self):
    """Return an iteration of all verticies in the graph"""
    return self._outgoing.keys()


  def edge_count(self):
    """Return the number of edges in the graph"""
    total = sum(len(self._outgoing[v]) for v in self._outgoing)
    return total if self.is_directed() else total // 2


  def edges(self):
    """Return a set of all edges of the graph"""
    result = set()
    for secondary_map in self._outgoing.values():
      result.update(secondary_map.values())
    return result


  def get_edge(self, u, v):
    """return edge from u to v. None if not adjacent"""
    return self._outgoing[u].get(v)
    

  def degree(self, v, outgoing = True):
    """Return number of outgoing edges incident to vertex v"""
    adj = self._outgoing if outgoing else self._incoming
    return len(adj[v])
    

  def incident_edges(self, v, outgoing = True):
    """Return all outgoing edges incident to vertex v"""
    adj = self._outgoing if outgoing else self._incoming
    for edge in adj[v].values():
      yield edge


  def insert_vertex(self, x = None):
    """Insert and return a new vertex with element x"""
    v = self._Vertex(x)
    self._outgoing[v] = {}
    if self.is_directed():
      self._incoming[v] = {}
    return v


  def insert_edge(self, u, v, x = None):
    """Insert and return a new edge from u to v with auxillary element x"""
    e = self.Edge(u, v, x)
    self._outgoing[u][v] = e
    self._incoming[v][u] = e



  class Vertex:
    """Lightweight vertex structure for a graph"""
    #http://book.pythontips.com/en/latest/__slots__magic.html
    __slots__ = '_element'


    def __init__(self, x):
      """Do not call constructor directly. Use Graph's insert_vertex() method"""
      self._element = x


    def element(self):
      """Return element asociated with this vertex"""
      return self._element


    def __hash__(self): #Will allow vertex to be map/set key
      return hash(id(self))



  class Edge:
    """Lightweight edge structures for a graph"""
    __slots__ = 'origin', 'destination', '_element'


    def __init__(self,u, v, x):
      """Do not call constructor directly. Use Graph's insert_edge(u, v, x)"""
      self._origin = u
      self._destination = v
      self._element = x


    def endpoints(self):
      """Return (u, v) tuple for verticies u and v"""
      return (self._origin, self._destination)


    def opposite(self):
      """Return the vertex that is opposite v on this edge"""
      return self._destination if v is self._origin else self._origin


    def element(self):
      """Return element asociated with this edge"""
      return self._element


    def __hash__(self):
      return hash((self._element, self._destination))
