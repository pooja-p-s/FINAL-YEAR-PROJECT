import matlab.engine
import sys
def fdfplbp():
    positionOfPath = 1
    sys.path.insert( positionOfPath, '/Users/poojaps/Documents/MATLAB' )
    eng = matlab.engine.start_matlab()
    eng.callFDFPLBP(nargout=0)
    eng.quit()
    
def sdfplbp():
    positionOfPath = 1
    sys.path.insert( positionOfPath, '/Users/poojaps/Documents/MATLAB' )
    eng = matlab.engine.start_matlab()
    eng.callSDFPLBP(nargout=0)
    eng.quit()


def find_fplbp():
    positionOfPath = 1
    sys.path.insert( positionOfPath, '/Users/poojaps/Documents/MATLAB' )
    eng = matlab.engine.start_matlab()
    eng.singleFP(nargout=0)
    eng.quit()