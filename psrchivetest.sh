#!/bin/bash

echo 'Test of psrchive install'
ARCHIVE=./datatest/archive.Dp
SCRUNCHED=./datatest/archive.DFTp
PROFILE=./datatest/archive.DFTp.sm
TIMFILE=./datates/timfile.tim
PARFILE=./datatest/parfile.par

if [ -f "$ARCHIVE" ]; then
	psrstat -c freq,nbin,nchan,snr $ARCHIVE
	echo "To change between frequency and time enter 't' and 'f'"
	echo "Press 'Q' to leave"
	pazi $ARCHIVE
	pam -FTp -e 'DFTp' $ARCHIVE
	psrsmooth  -W $SCRUNCHED
	pav -DFT $PROFILE
	rm $PROFILE $SCRUNCHED
fi

read -p "Press enter to continue"

if [ -f "$TIMFILE" ] && [ -f "$PARFILE" ]; then
	tempo2 -gr plk -f "$PARFILE" "$TIMFILE"
fi
