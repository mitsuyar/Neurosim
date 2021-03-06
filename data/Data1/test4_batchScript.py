ó
fKvYc           @   sÅ   d  Z  d d l Z d d l m Z m Z d d l m Z d d l m Z d d l Z d d l	 m
 Z
 d d l m Z e j   Z e j   d k r¢ e j d  n  d	   Z d
 e f d     YZ d S(   s[   
batch.py 

Class to setup and run batch simulations

Contributors: salvadordura@gmail.com
iÿÿÿÿN(   t   izipt   product(   t   popen2(   t   sleep(   t   specs(   t   hi    c         C   st   d d l  m } m } d Gt j   GHd |  | | f } | d GH| | j d  d | d | } | j j   GHd  S(	   Niÿÿÿÿ(   t   Popent   PIPEs   
Job in rank id: s"   nrniv %s simConfig=%s netParams=%ss   
t    t   stdoutt   stderr(   t
   subprocessR   R   t   pct   idt   splitR	   t   read(   t   scriptt   cfgSavePatht   netParamsSavePathR   R   t   commandt   proc(    (    s7   //anaconda/lib/python2.7/site-packages/netpyne/batch.pyt   runJob   s    	!t   Batchc           B   s,   e  Z d  d d d  Z d   Z d   Z RS(   s   cfg.pys   netParams.pyc         C   s¡   d t  t j j    |  _ | |  _ | |  _ d |  j |  _ d |  _ i  |  _	 g  |  _
 | r x; | j   D]* \ } } |  j
 j i | d 6| d 6 ql Wn  d  S(   Nt   batch_t   /t   gridt   labelt   values(   t   strt   datetimet   datet   todayt
   batchLabelt   cfgFilet   netParamsFilet
   saveFoldert   methodt   runCfgt   paramst	   iteritemst   append(   t   selfR!   R"   R&   t   kt   v(    (    s7   //anaconda/lib/python2.7/site-packages/netpyne/batch.pyt   __init__"   s    					c   	      C   só   d d  l  } | j j |  } | j |  d } | j d  d } y | j |  Wn/ t k
 r | j j |  s d G| GHq n Xi |  j d 6} | d k rï d d  l } d | GHt	 | d	  # } | j
 | | d
 d d t Wd  QXn  d  S(   Niÿÿÿÿi    t   .i   s    Could not createt   batcht   jsons   Saving batch to %s ... t   wt   indenti   t	   sort_keys(   t   ost   patht   basenameR   t   mkdirt   OSErrort   existst   __dict__R/   t   opent   dumpt   True(	   R)   t   filenameR3   R5   t   foldert   extt   dataSaveR/   t   fileObj(    (    s7   //anaconda/lib/python2.7/site-packages/netpyne/batch.pyt   save.   s    	c   6      C   sv	  |  j  d> k rr	d d  l } d d  l } y | j |  j  Wn5 t k
 rr | j j |  j  ss d G|  j GHqs n X|  j d |  j d } |  j	 |  |  j d |  j d } | j
 d | j j t  d	 |  |  j d |  j d
 } | j
 d |  j d	 |  | j j |  j  j d  d } t j | |  j  } | j |  _ |  j  d k r<t } t } xI |  j D]> }	 d |	 k rt |	 d <t } qq|	 d t k rqt } qqqqW| rt g  |  j D]* }	 |	 d t k rÆ|	 d |	 d f ^ qÆ  \ }
 } n d? }
 d@ } t g  |  j D]* }	 |	 d t k r|	 d |	 d f ^ q  \ }
 } t t |    } t t g  | D] } t t |   ^ qs   } | r't g  |  j D]* }	 |	 d t k rª|	 d |	 d f ^ qª  \ } } t |   } t g  | D] } t t |   ^ qù  } | |
 }
 q<dA g } dB g } n  |  j j d d   d k rx- t t  t! j"     D] } t! j#   qpWn  x°t | |  D]\ } } xt | |  D]\ } } | rÜ| | } | | } n | } | } | G| GHxÐ t$ |  D]Â \ } } |
 | } t% | t&  r|  j } xT t t |  d  D]< } t% | t' j(  rqt) | | |  } qC| | | } qCW| | | d <n t* |  j | |  t+ |  d t+ |  GHqþW|  j d j, g  | D] } d j, d t+ |   ^ q× } |  j d | }  |  j j d t  rE| j |  d  rEd |  GHq³|  j j d t  ry| j |  d  ryd |  GHq³|  j j d d   rÁ| j |  |  j d  rÁd |  |  j d f GHq³| |  j _- |  j |  j _ |  j d | d }! |  j j	 |!  |  j j d d   d k r@|  j j d d  }" t. |"  |  j j d  d  }# |  j j d! d  }$ |  j j d" d#  }% |  j j d$ d%  }& |  j j d& d'  }' |  j j d( d)  }( d* |# |$ f }) |# |$ }* d+ |& |* |% |! | f }+ t/ d,  \ }, }- d- |  |' |( |) |  |  |+ f }. |- j0 |.  |. d. GH|- j1   q³|  j j d d   d/ k rÕ|  j j d d  }" t. |"  |  j j d0 d1  }/ |  j j d  d  }# |  j j d2 d  }0 |  j j d3 d4  }1 |  j j d5 d  }2 |  j j d" d#  }% |  j j d$ d6  }& |  j j d& d'  }' |# |0 }* d+ |& |* |% |! | f }+ d7 |  |/ |' |# |0 |  |  |1 |2 |+ f
 }. d8 G|  GH|. d. GHd9 |  }3 t2 |3 d:   }4 |4 j0 d; |.  Wd  QXt/ d< |3  \ }, }5 |5 j1   q³|  j j d d   d k r³|  j d | }  d8 G|  GHt! j3 t4 |  j j d" d#  |! |  q³q³WqWy! x t! j5   rY	t. d  q@	WWn n Xt. d=  n  d  S(C   NR   t   listiÿÿÿÿs    Could not createR   s   _batch.jsons   _batchScript.pys   cp R   s   _netParams.pyR-   i    t   groupR   R   t   typet   mpii   s    = t    t   _t   skips   .jsons3   Skipping job %s since output file already exists...t   skipCfgs	   _cfg.jsons0   Skipping job %s since cfg file already exists...t
   skipCustoms/   Skipping job %s since %s file already exists...t
   hpc_torquet   sleepIntervalt   nodest   ppnR   s   init.pyt
   mpiCommandt   mpiexect   walltimes   00:30:00t	   queueNamet   defaults   nodes=%d:ppn=%ds9   %s -np %d nrniv -python -mpi %s simConfig=%s netParams=%st   qsubs  #!/bin/bash 
                            #PBS -N %s
                            #PBS -l walltime=%s
                            #PBS -q %s
                            #PBS -l %s
                            #PBS -o %s.run
                            #PBS -e %s.err
                            cd $PBS_O_WORKDIR
                            echo $PBS_O_WORKDIR
                            %ss   
t	   hpc_slurmt
   allocationt   csd403t   coresPerNodet   emails   a@b.cR>   t   ibrunsþ   #!/bin/bash 
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
                            s   Submitting job s	   %s.sbatchR0   s   %ss   sbatch i
   (   R   RC   (    (    (   i    (   i    (6   R$   R3   t   globR6   R#   R7   R4   R8   R    RB   t   systemt   realpatht   __file__R"   R5   R!   R   t   impt   load_sourcet   cfgt   FalseR&   R<   t   zipRC   R   t   ranget   lenR    R%   t   gett   Nonet   intR   t   nhostt	   runworkert	   enumeratet
   isinstancet   tupleR   t	   SimConfigt   getattrt   setattrR   t   joint   simLabelR   R   t   writet   closeR:   t   submitR   t   working(6   R)   R3   R\   t
   targetFileR   t   cfgModuleNamet	   cfgModulet   groupedParamst   ungroupedParamst   pt	   labelListt
   valuesListt   valueCombinationst   xt   indexCombinationst   labelListGroupt   valuesListGroupt   valueCombGroupst   indexCombGroupst   iworkert   iCombGt   pCombGt   iCombNGt   pCombNGt   iCombt   pCombt   it   paramValt
   paramLabelt	   containert   ipRs   t   jobNameR   RM   RN   RO   R   RP   RR   RS   t   nodesppnt   numprocR   t   outputt   inputt	   jobStringRW   RY   RZ   R>   t	   batchfilet	   text_filet   pinput(    (    s7   //anaconda/lib/python2.7/site-packages/netpyne/batch.pyt   runE   sò    %"
	IF1F+	
	
	<((/

	

(		
	0N(   t   __name__t
   __module__Rh   R,   RB   R   (    (    (    s7   //anaconda/lib/python2.7/site-packages/netpyne/batch.pyR       s   	(   t   __doc__R   t	   itertoolsR    R   R   t   timeR   R`   t   netpyneR   t   neuronR   t   ParallelContextR   R   t   master_works_on_jobsR   t   objectR   (    (    (    s7   //anaconda/lib/python2.7/site-packages/netpyne/batch.pyt   <module>   s    	
