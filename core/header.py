#!/usr/bin/env python

import random
def main_header():
	header_1 = r"""

           ____,'`-,
      _,--'   ,/::.;
   ,-'       ,/::,' `---.___        ___,_
   |       ,:';:/        ;'"`;"`--./ ,-^.;--.
   |:     ,:';,'         '         `.   ;`   `-.
    \:.,:::/;/ -:.                   `  | `     `-.
     \:::,'//__.;  ,;  ,  ,  :.`-.   :. |  ;       :.
      \,',';/O)^. :'  ;  :   '__` `  :::`.       .:' )
      |,'  |\__,: ;      ;  '/O)`.   :::`;       ' ,'
           |`--''            \__,' , ::::(       ,'
           `    ,            `--' ,: :::,'\   ,-'
            | ,;         ,    ,::'  ,:::   |,'
            |,:        .(          ,:::|   `
            ::'_   _   ::         ,::/:|
           ,',' `-' \   `.      ,:::/,:|
          | : _  _   |   '     ,::,' :::
          | \ O`'O  ,',   ,    :,'   ;::
           \ `-'`--',:' ,' , ,,'      ::
            ``:.:.__   ',-','        ::'
              `--.__, ,::.         ::'
                   |:  ::::.       ::'
                   |:  ::::::    ,::'
				   """

	header_2 = r"""
          _ ._  _ , _ ._
        (_ ' ( `  )_  .__)
      ( (  (    )   `)  ) _)
     (__ (_   (_ . _) _) ,__)
         `~~`\ ' . /`~~`
              ;   ;
              /   \
_____________/_ __ \_____________ Windows Destruction"""
	header_3 = r"""
	                                  ,        ,
                                /(        )`
                                \ \___   / |
                                /- _  `-/  '
                               (/\/ \ \   /\
                               / /   | `    \
                               O O   ) /    |
                               `-^--'`<     '
                   TM         (_.)  _  )   /
|  | |\  | ~|~ \ /             `.___/`    /
|  | | \ |  |   X                `-----' /
`__| |  \| _|_ / \  <----.     __ / __   \
                    <----|====O)))==) \) /====
                    <----'    `--' `.__,' \
                                 |        |
                                  \       /
                             ______( (_  / \______
                           ,'  ,-----'   |        \
                           `--{__________)        \/"""



	header_4 = r"""
       .--.       .--.
    _  `    \     /    `  _
     `\.===. \.^./ .===./`
            \/`"`\/
         ,  | ( ) |  ,
        / `\|;-.-'|/` \
       /    |::\  |    \
    .-' ,-'`|:::; |`'-, '-.
        |   |::::\|   |
        |   |::::;|   |
        |   \:::://   |
        |    `.://'   |
       .'             `.
    _,'                 `,_"""

	header_5 = r"""
          XX                                    XX
        XX..X                                  X..XX
      XX.....X                                X.....XX
 XXXXX.....XX                                  XX.....XXXXX
X |......XX%,.@                              @#%,XX......| X
X |.....X  @#%,.@                          @#%,.@  X.....| X
X  \...X     @#%,.@                      @#%,.@     X.../  X
 X# \.X        @#%,.@                  @#%,.@        X./  #
  ##  X          @#%,.@              @#%,.@          X   #
, "# #X            @#%,.@          @#%,.@            X ##
   `###X             @#%,.@      @#%,.@             ####'
  . ' ###              @#%.,@  @#%,.@              ###`"
    . ";"                @#%.@#%,.@                ;"` ' .
      '                    @#%,.@                   ,.
      ` ,                @#%,.@  @@                `
                          @@@  @@@                  .
	"""

	hdr_num = random.randint(1, 5)
	if hdr_num ==1:
		print header_1
	if hdr_num ==2:
		print header_2
	if hdr_num ==3:
		print header_3
	if hdr_num ==4:
		print header_4
	if hdr_num ==5:
		print header_5
