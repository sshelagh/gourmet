import optparse
import version
try:
    import optcomplete
    has_optcomplete = True
except ImportError:
    has_optcomplete = False

parser = optparse.OptionParser(
    version=version.version,
    option_list=[
    #optparse.make_option("-h","--help",action="help"),
    optparse.make_option("--choose-database",const="True",action='store_const',
                         dest="choosedb",help="Show Database chooser dialog",
                         default=""),
    optparse.make_option("--use-threads",
                         action="store_const",const=True,
                         dest="threads",
                         help="Enable threading support.",
                         default=False),
    optparse.make_option("--sqlite",
                         action="store_const",const="sqlite",
                         dest="db",help="Use SQLITE database backend",
                         default="metakit"),
    optparse.make_option("--metakit",
                         action="store_const",const="metakit",
                         dest="db",help="Use metakit backend",
                         default="metakit"),
    optparse.make_option("--gourmet-directory",
                         action="store",
                         dest="gourmetdir",
                         help="Gourmet configuration directory",
                         default=""),
    optparse.make_option("--debug-threading-interval",
                         action="store",
                         type="float",
                         dest='thread_debug_interval',
                         help="Interval for threading debug calls",
                         default=5.0),
    optparse.make_option("--debug-threading",action="store_true",dest='thread_debug',
                         help="Print debugging information about threading."),
    optparse.make_option("--debug-file",action="store",type="string",dest="debug_file",
                         help="Regular expression that matches filename(s) whose code we want to display debug messages from.",
                         default=""),
    optparse.make_option("-q",action='store_const',const=-1,
                         dest='debug',
                         help="Don't print gourmet error messages"),
    optparse.make_option("--showtimes",action="store_true",dest="time",
                         help="Print timestamps on debug statements."),
    optparse.make_option("-v",action='count',
                         help="Be verbose (extra v's will increase the verbosity level",
                         dest='debug'),
    optparse.make_option("--data-directory",
                         dest="datad",
                         help="Directory for Gourmet data files.",
                         action="store",
                         default=""),
    optparse.make_option("--image-directory",
                         dest="imaged",
                         help="Directory for Gourmet image files.",
                         action="store",
                         default=""),
    optparse.make_option("--glade-directory",
                         dest="gladed",
                         help="Directory for Gourmet glade files.",
                         action="store",
                         default=""),
    optparse.make_option("--disable-psyco",
                         dest="psyco",
                         action="store_false",
                         help="Do not use psyco if it is installed.",
                         default=True),
    ]
    )
if has_optcomplete:
    optcomplete.autocomplete(parser)

(options, args) = parser.parse_args()
