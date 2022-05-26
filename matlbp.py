import matlab.engine
import sys
 
def fdlbp():
    positionOfPath = 1
    sys.path.insert( positionOfPath, '/Users/poojaps/Documents/MATLAB' )
    eng = matlab.engine.start_matlab()
    eng.callFDLBP(nargout=0)
    eng.quit()
         
def fdtplbp():
    positionOfPath = 1
    sys.path.insert( positionOfPath, '/Users/poojaps/Documents/MATLAB' )
    eng = matlab.engine.start_matlab()
    eng.callFDTPLBP(nargout=0)
    eng.quit()
    
def fdfplbp():
    positionOfPath = 1
    sys.path.insert( positionOfPath, '/Users/poojaps/Documents/MATLAB' )
    eng = matlab.engine.start_matlab()
    eng.callFDFPLBP(nargout=0)
    eng.quit()

  
def sdlbp():
    positionOfPath = 1
    sys.path.insert( positionOfPath, '/Users/poojaps/Documents/MATLAB' )
    eng = matlab.engine.start_matlab()
    eng.callSDLBP(nargout=0)
    eng.quit()
      
def sdtplbp():
    positionOfPath = 1
    sys.path.insert( positionOfPath, '/Users/poojaps/Documents/MATLAB' )
    eng = matlab.engine.start_matlab()
    eng.callSDTPLBP(nargout=0)
    eng.quit()  
    
def sdfplbp():
    positionOfPath = 1
    sys.path.insert( positionOfPath, '/Users/poojaps/Documents/MATLAB' )
    eng = matlab.engine.start_matlab()
    eng.callSDFPLBP(nargout=0)
    eng.quit()


