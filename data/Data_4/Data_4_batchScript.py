ó
ÿ^úYc           @   sÔ   d  Z  d d l Z d d l m Z m Z d d l m Z m Z d d l m	 Z	 d d l
 Z
 d d l m Z d d l m Z e j   Z e j   d k r¨ e j d  n  d	   Z d
   Z d e f d     YZ d S(   s[   
batch.py 

Class to setup and run batch simulations

Contributors: salvadordura@gmail.com
iÿÿÿÿN(   t   izipt   product(   t   Popent   PIPE(   t   sleep(   t   specs(   t   hi    c         C   s^   d Gt  j   GHd |  | | f } | d GHt | j d  d t d t } | j j   GHd  S(   Ns   
Job in rank id: s"   nrniv %s simConfig=%s netParams=%ss   
t    t   stdoutt   stderr(   t   pct   idR   t   splitR   R   t   read(   t   scriptt   cfgSavePatht   netParamsSavePatht   commandt   proc(    (    s?   //anaconda/lib/python2.7/site-packages/netpyne/netpyne/batch.pyt   runJob   s
    	!c         C   sÔ   t  |   t k rK x» |  D]+ } t  |  t t g k r t |  q q Wn t  |   t k rÐ xp |  j   D]_ \ } } t  |  t t g k r t |  n  t  |  t k rj |  j |  |  t |  <qj qj Wn  |  S(   N(   t   typet   listt   dictt
   tupleToStrt	   iteritemst   tuplet   popt   str(   t   objt   itemt   keyt   val(    (    s?   //anaconda/lib/python2.7/site-packages/netpyne/netpyne/batch.pyR      s    #t   Batchc           B   s;   e  Z d  d d d i  d  Z d   Z d   Z d   Z RS(   s   cfg.pys   netParams.pyc   	      C   sä   d t  t j j    |  _ | |  _ | |  _ | |  _ d |  j |  _ d |  _	 i  |  _
 g  |  _ | r¦ x; | j   D]* \ } } |  j j i | d 6| d 6 qu Wn  | rà x1 |  j D]# } | d | k r¶ t | d <q¶ q¶ Wn  d  S(   Nt   batch_t   /t   gridt   labelt   valuest   group(   R   t   datetimet   datet   todayt
   batchLabelt   cfgFilet   initCfgt   netParamsFilet
   saveFoldert   methodt   runCfgt   paramsR   t   appendt   True(	   t   selfR+   R-   R1   t   groupedParamsR,   t   kt   vt   p(    (    s?   //anaconda/lib/python2.7/site-packages/netpyne/netpyne/batch.pyt   __init__0   s    						% c         C   s  d d  l  } d d l m } | j j |  } | j |  d } | j d  d } y | j |  Wn/ t k
 r | j j |  s d G| GHq n X| |  j	  } i t
 |  d 6} | d k rd d  l }	 d	 | GHt | d
  # }
 |	 j | |
 d d d t Wd  QXn  d  S(   Niÿÿÿÿ(   t   deepcopyi    t   .i   s    Could not createt   batcht   jsons   Saving batch to %s ... t   wt   indenti   t	   sort_keys(   t   ost   copyR:   t   patht   basenameR   t   mkdirt   OSErrort   existst   __dict__R   R=   t   opent   dumpR3   (   R4   t   filenameRA   R:   RD   t   foldert   extt   odictt   dataSaveR=   t   fileObj(    (    s?   //anaconda/lib/python2.7/site-packages/netpyne/netpyne/batch.pyt   save@   s"    	c         C   s   t  | t  r |  j } xT t t |  d  D]< } t  | t j  r] t | | |  } q/ | | | } q/ W| | | d <n t |  j | |  d  S(   Ni   iÿÿÿÿ(	   t
   isinstanceR   t   cfgt   ranget   lenR   t	   SimConfigt   getattrt   setattr(   R4   t
   paramLabelt   paramValt	   containert   ip(    (    s?   //anaconda/lib/python2.7/site-packages/netpyne/netpyne/batch.pyt   setCfgNestedParamY   s    	c   4      C   s¦	  |  j  dB k r¢	d d  l } d d  l } y | j |  j  Wn5 t k
 rr | j j |  j  ss d G|  j GHqs n X|  j d |  j d } |  j	 |  |  j d |  j d } | j
 d | j j t  d	 |  |  j d |  j d
 } | j
 d |  j d	 |  | j j |  j  j d  d } t j | |  j  } | j |  _ t |  j _ t |  j  d k r x0 |  j j   D] \ } } |  j | |  q}Wn  |  j  d k rt }	 t }
 xI |  j D]> } d | k rêt | d <t }
 qÅ| d t k rÅt }	 qÅqÅW|
 rVt g  |  j D]* } | d t k r| d | d f ^ q  \ } } n dC } dD } t g  |  j D]* } | d t k ro| d | d f ^ qo  \ } } t t |    } t t g  | D] } t t |   ^ qÇ   } |	 r{t g  |  j D]* } | d t k rþ| d | d f ^ qþ  \ } } t  |   } t  g  | D] } t t |   ^ qM  } | | } qdE g } dF g } n  |  j! j" d d   d k rÛx- t t$ t% j&     D] } t% j'   qÄWn  xt | |  D]{\ } } xlt | |  D][\ } } |	 r0| | } | | } n | } | } | G| GHxM t( |  D]? \ } } | | } |  j | |  t) |  d t) |  GHqRW|  j d j* g  | D] } d j* d t) |   ^ q¨ } |  j d | } |  j! j" d t  r| j | d  rd | GHnB|  j! j" d t  rJ| j | d  rJd | GHn|  j! j" d d   r| j | |  j! d  rd | |  j! d f GHnÆ| |  j _+ |  j |  j _ |  j d | d } |  j j	 |  |  j! j" d d   d k rU|  j! j" d d  }  t, |   |  j! j" d  d  }! |  j! j" d! d  }" |  j! j" d" d#  }# |  j! j" d$ d%  }$ |  j! j" d& d'  }% |  j! j" d( d)  }& d* |! |" f }' |! |" }( d+ |$ |( |# | | f }) d, | |% |& |' | | |) f }* d- G| GH|* d. GHd/ | }+ t- |+ d0   }, |, j. d1 |*  Wd  QXt/ d2 |+ g d3 t0 d4 t0 }- |- j1 |- j2 }. }/ n|  j! j" d d   d5 k rû|  j! j" d d  }  t, |   |  j! j" d6 d7  }0 |  j! j" d  d  }! |  j! j" d8 d  }1 |  j! j" d9 d:  }2 |  j! j" d; d  }3 |  j! j" d" d#  }# |  j! j" d$ d<  }$ |  j! j" d& d'  }% |! |1 }( d+ |$ |( |# | | f }) d= | |0 |% |! |1 | | |2 |3 |) f
 }* d- G| GH|* d. GHd> | }+ t- |+ d0   }, |, j. d1 |*  Wd  QXt/ d? |+ g d@ t0 d4 t0 }- |- j1 |- j2 }. }/ n] |  j! j" d d   d k rX	|  j d | } d- G| GHt% j3 t4 |  j! j" d" d#  | |  n  t, d  qWqëWy! x t% j5   r	t, d  qp	WWn n Xt, dA  n  d  S(G   NR#   R   iÿÿÿÿs    Could not createR"   s   _batch.jsons   _batchScript.pys   cp R   s   _netParams.pyR;   i    R&   R$   R%   R   t   mpis    = t    t   _t   skips   .jsons3   Skipping job %s since output file already exists...t   skipCfgs	   _cfg.jsons0   Skipping job %s since cfg file already exists...t
   skipCustoms/   Skipping job %s since %s file already exists...t
   hpc_torquet   sleepIntervali   t   nodest   ppnR   s   init.pyt
   mpiCommandt   mpiexect   walltimes   00:30:00t	   queueNamet   defaults   nodes=%d:ppn=%ds9   %s -np %d nrniv -python -mpi %s simConfig=%s netParams=%ss¥   #!/bin/bash 
#PBS -N %s
#PBS -l walltime=%s
#PBS -q %s
#PBS -l %s
#PBS -o %s.run
#PBS -e %s.err
cd $PBS_O_WORKDIR
echo $PBS_O_WORKDIR
%s
                            s   Submitting job s   
s   %s.pbsR>   s   %st   qsubR	   R   t	   hpc_slurmt
   allocationt   csd403t   coresPerNodet   emails   a@b.cRL   t   ibrunsþ   #!/bin/bash 
#SBATCH --job-name=%s
#SBATCH -A %s
#SBATCH -t %s
#SBATCH --nodes=%d
#SBATCH --ntasks-per-node=%d
#SBATCH -o %s.run
#SBATCH -e %s.err
#SBATCH --mail-user=%s
#SBATCH --mail-type=end

source ~/.bashrc
cd %s
%s
wait
                            s	   %s.sbatcht   sbatcht   stdini
   (   R#   R   (    (    (   i    (   i    (6   R/   RA   t   globRE   R.   RF   RC   RG   R*   RQ   t   systemt   realpatht   __file__R-   RD   R+   R   t   impt   load_sourceRS   t   Falset   checkErrorsRU   R,   R   R]   R1   R3   t   zipR   R   RT   R    R0   t   gett   Nonet   intR
   t   nhostt	   runworkert	   enumerateR   t   joint   simLabelR   RI   t   writeR   R   Ru   R   t   submitR   t   working(4   R4   RA   Rv   t
   targetFileR   t   cfgModuleNamet	   cfgModuleRY   RZ   R5   t   ungroupedParamsR8   t	   labelListt
   valuesListt   valueCombinationst   xt   indexCombinationst   labelListGroupt   valuesListGroupt   valueCombGroupst   indexCombGroupst   iworkert   iCombGt   pCombGt   iCombNGt   pCombNGt   iCombt   pCombt   iR   t   jobNameR   Re   Rf   Rg   R   Rh   Rj   Rk   t   nodesppnt   numprocR   t	   jobStringt	   batchfilet	   text_fileR   t   outputt   inputRo   Rq   Rr   RL   (    (    s?   //anaconda/lib/python2.7/site-packages/netpyne/netpyne/batch.pyt   rune   sô    %"
	IF1F+	
	
<((/

		


(		
	(N(   t   __name__t
   __module__R   R9   RQ   R]   R§   (    (    (    s?   //anaconda/lib/python2.7/site-packages/netpyne/netpyne/batch.pyR    .   s   		(   t   __doc__R'   t	   itertoolsR    R   t
   subprocessR   R   t   timeR   Rz   t   netpyneR   t   neuronR   t   ParallelContextR
   R   t   master_works_on_jobsR   R   t   objectR    (    (    (    s?   //anaconda/lib/python2.7/site-packages/netpyne/netpyne/batch.pyt   <module>   s    		