import os
import glob
wd = os.getcwd()


def main():
	for file in glob.glob("*.pdf"):

		print(f"Printing {file}")
		#os.system(f'lpr -PHP_Color_LaserJet_M452dn -o Duplex=DuplexNoTumble -o page-ranges=1-2 \"{file}\"')
		os.system(f'lpr -o InputSlot=Tray2 -o sides=two-sided-long-edge \"{file}\"')


if __name__ == '__main__':
    main()
