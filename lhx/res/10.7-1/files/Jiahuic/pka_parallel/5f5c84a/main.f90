! This is main drive for compute pka by parallelization
program pka_tabi_parallel
use molecule
use comdata
use bicg
use treecode
use treecode3d_procedures
  integer i,j
  character(100) fhead

  !??????????????????????????????????????????????????????????????
  !PARAMETERS: now can be read from usrdate.in file

  !PB equation
  !eps0=1.d0;            !the dielectric constant in molecule
  !eps1=80.d0;           !the dielectric constant in solvent
  !bulk_strength=0.15d0  !ion_strength with units (M)$I=\sum\limits_{i=1}^nc_iz_i^2$

  !Treecode
  !order=3               !The order of taylor expansion
  !maxparnode=500        !maximum particles per leaf
  !theta=0.8d0           !MAC, rc/R<MAC, the bigger MAC, the more treecode
  open(101,file="usrdata.in")
  READ(101,*,IOSTAT = MEOF) fhead, protein
  READ(101,*,IOSTAT = MEOF) fhead, den
  READ(101,*,IOSTAT = MEOF) fhead, eps0
  READ(101,*,IOSTAT = MEOF) fhead, eps1
  READ(101,*,IOSTAT = MEOF) fhead, bulk_strength
  READ(101,*,IOSTAT = MEOF) fhead, order
  READ(101,*,IOSTAT = MEOF) fhead, maxparnode
  READ(101,*,IOSTAT = MEOF) fhead, theta
  close(101)
  !print *,fname,den,eps0,eps1,bulk_strength,order,maxparnode,theta
  !???????????????????????????????????????????????????????????????

  lenfname = len(protein)
  do while (protein(lenfname:lenfname) .eq. ' ')
      lenfname = lenfname - 1
  enddo
  rslt=system('python filenames.py '//protein(1:lenfname))
  nsite = 0
  OPEN(102,FILE=protein(1:lenfname)//".names")
  do
      read(102,*,IOSTAT = MEOF) sitename

      if ((MEOF .eq. 0)) then
          nsite=nsite+1
      endif
      IF(MEOF .LT. 0) EXIT
  enddo
  CLOSE(102)

  ALLOCATE(sitelength(nsite),STAT=ierr)
  ALLOCATE(sitelist(nsite),STAT=ierr)
  OPEN(102,FILE=protein(1:lenfname)//".names")
  do i=1,nsite
      read(102,*,IOSTAT = MEOF) sitename
      sitelength(i) = len(sitename)
      do while (sitename(sitelength(i):sitelength(i)) .eq. ' ')
          sitelength(i) = sitelength(i) - 1
      enddo

      sitelist(i) = sitename
  enddo
  CLOSE(102)
  rslt=system('rm '//protein(1:lenfname)//".names")

  fname = sitelist(1)
  call tabipb
  fname = sitelist(2)
  call tabipb

  DEALLOCATE(sitelength)
  DEALLOCATE(sitelist)

end program pka_tabi_parallel
