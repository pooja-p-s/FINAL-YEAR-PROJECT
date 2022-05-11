import matlab.engine
import sys
def fdtplbp():
    positionOfPath = 1
    sys.path.insert( positionOfPath, '/Users/poojaps/Documents/MATLAB' )
    eng = matlab.engine.start_matlab()
    eng.callFDTPLBP(nargout=0)
    eng.quit()
    
def sdtplbp():
    positionOfPath = 1
    sys.path.insert( positionOfPath, '/Users/poojaps/Documents/MATLAB' )
    eng = matlab.engine.start_matlab()
    eng.callSDTPLBP(nargout=0)
    eng.quit()

def find_tplbp():
    positionOfPath = 1
    sys.path.insert( positionOfPath, '/Users/poojaps/Documents/MATLAB' )
    eng = matlab.engine.start_matlab()
    eng.singleTP(nargout=0)
    eng.quit()
    
