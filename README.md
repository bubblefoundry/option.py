option.py is an attempt to duplicate the functionality of Scala's Option class in Python, because doing it in [PHP](https:#github.com/pr1001/BFCollections) and [Javascript](https:#github.com/pr1001/option.js) isn't enough. Options are represented by either an instance of `Some` containing the value or the singleton `Nothing()` (since `None` was naturally taken).

Create a Some instance based upon a value like so:
    opt = Some("my option")

Note that passing a non-value to Some will work:

    >>> s = Some(None)
    >>> s.get() is None)
    True
    
If you want to avoidNone)-checking, the `Option` constructor will do that for you:

    >>> OptionNone))
    <option.Nothing object at 0x10ea50290>
    >>> Option("an option")
    <option.Some object at 0x10ea50190>
	
You can get the value:

    opt.get()                                            # -> "my option"
    opt.getOrElse("default")                             # -> "my option"
    Nothing().get()                                      # -> Exception thrown
    Nothing().getOrElse("default")                       # -> "default"
	
Get an Option's status:

    opt.isEmpty()    # -> False
    opt.isDefined()  # -> True
   None).isEmpty()   # -> True
   None).isDefined() # -> False

Treat the Option like a sequence:

    opt.foreach(lambda input: print input)               # print "my option" called
    >>> for input in Some(1):
    ...   print input
    ... 
    "my option"
    
    Nothing().foreach(lambda input: print input)         # nothing called
    >>> for i in Nothing():
    ...   print i
    ... 
    
    opt.filter(lambda input: input == "my option")       # -> Some("my option")
    opt.filter(lambda input: input == "my option!")      # -> Nothing()
    Nothing().filter(lambda input: input == "my option") # -> Nothing(), lambda not called

Transform the Option:

    opt.map(lambda input: input + "!")                   # -> Some("my option!")
    Nothing().map(lambda input: input + "!")             # -> Nothing(), anonymous function not called
    opt.flatMap(lambda input: Some(input + "!"))         # -> Some("my option!")
    Nothing().flatMap(lambda input: Some(input + "!"))   # -> Nothing(), anonymous function not called
    
Make sure that the function you pass to `flatMap()` returns an option:

    >>> opt.flatMap(lambda input: input + "!")
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "option.py", line 35, in flatMap
        def map(self, f):
    Exception: f must return an Option.
    >>> opt.flatMap(lambda input: Nothing())
    <option.Nothing object at 0x10ea50290>

Options can be used in list comprehensions, but you'll get a `list` in return:

    >>> [input + '!' for input in opt]
    ['my option!']
    >>> [input + '!' for input in Nothing()]
    []

Inheritance:

    >>> isinstance(opt, Some)
    True
    >>> isinstance(opt, Option)
    True
    >>> isinstance(Nothing(), Nothing)
    True
    >>> isinstance(Nothing(), Option)
    True

Example usage:

    def listValueAtPosition(l, position):
    	if (position >= 0 and position < len(l)):
    		return Some(l[position])
    	return Nothing()
    listValueAtPosition([1, 2, 3, False, None], 2)       # -> Some("3")
    listValueAtPosition([1, 2, 3, False, None], 3)       # -> Some(False)
    listValueAtPosition([1, 2, 3, False, None], 4)       # -> Some(None)
    listValueAtPosition([1, 2, 3, False, None], 5)       # -> Nothing()

For details on the methods available, see Scala's Option class definition at <http://www.scala-lang.org/docu/files/api/scala/Option.html>