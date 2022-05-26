import matlab.engine
import sys

def find_fdlbp():
    positionOfPath = 1
    sys.path.insert( positionOfPath, '/Users/poojaps/Documents/MATLAB' )
    eng = matlab.engine.start_matlab()
    eng.singleLBP(nargout=0)
    eng.quit()
    
def find_sdlbp():
    positionOfPath = 1
    sys.path.insert( positionOfPath, '/Users/poojaps/Documents/MATLAB' )
    eng = matlab.engine.start_matlab()
    eng.singleLBP(nargout=0)
    eng.quit()   
    
def find_fdtplbp():
    positionOfPath = 1
    sys.path.insert( positionOfPath, '/Users/poojaps/Documents/MATLAB' )
    eng = matlab.engine.start_matlab()
    eng.singleFDTP(nargout=0)
    eng.quit()

def find_fdfplbp():  
    positionOfPath = 1
    sys.path.insert( positionOfPath, '/Users/poojaps/Documents/MATLAB' )
    eng = matlab.engine.start_matlab()
    eng.singleFDFP(nargout=0)
    eng.quit()
    
def find_sdtplbp():
    positionOfPath = 1
    sys.path.insert( positionOfPath, '/Users/poojaps/Documents/MATLAB' )
    eng = matlab.engine.start_matlab()
    eng.singleSDTP(nargout=0)
    eng.quit()

def find_sdfplbp():  
    positionOfPath = 1
    sys.path.insert( positionOfPath, '/Users/poojaps/Documents/MATLAB' )
    eng = matlab.engine.start_matlab()
    eng.singleSDFP(nargout=0)
    eng.quit()
    
