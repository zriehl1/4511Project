try:
    from test_bishop import *
    from test_board import *
    from test_king import *
    from test_knight import *
    from test_pawn import *
    from test_rook import *
except:
    from .test_bishop import *
    from .test_board import *
    from .test_king import *
    from .test_knight import *
    from .test_pawn import *
    from .test_rook import *
