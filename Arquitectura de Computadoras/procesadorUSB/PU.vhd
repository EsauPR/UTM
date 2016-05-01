---------------------------------------------------------------------------------------------------
--
-- Title       : PU
-- Design      : UC
-- Author      : POT2
-- Company     : --
--
---------------------------------------------------------------------------------------------------
--
-- File        : PU.vhd
-- From        : interface description file
-- By          : Itf2Vhdl ver. 1.20
--
---------------------------------------------------------------------------------------------------
--
-- Description : 
--
---------------------------------------------------------------------------------------------------

--{{ Section below this comment is automatically maintained
--   and may be overwritten
--{entity {PU} architecture {PU}}

library IEEE;
use IEEE.STD_LOGIC_1164.all;



entity PU is
	 port(
		 clk : in STD_LOGIC;
		 CO : in STD_LOGIC_VECTOR(15 downto 0);
		 AddrRd : out STD_LOGIC_VECTOR(4 downto 0) ;
		 AddrRr : out STD_LOGIC_VECTOR(4 downto 0);
		 wr : out STD_LOGIC;						
		 sel : out STD_LOGIC;
		 constante : out STD_LOGIC_VECTOR(7 downto 0)
	     );
end PU;

--}} End of automatically maintained section

architecture PU of PU is
signal tmp : STD_LOGIC ;
begin

	constante <= CO(11 downto 8)&CO(3 downto 0);			 
	sel <= '1' when CO(15 downto 12) = "1110" else '0';
	tmp <= '1' when CO(15 downto 12) = "1110" else CO(8); 			
	AddrRd <= 	tmp&CO(7 downto 4);
	wr <= '1' ;--when CO(15 downto 12) = "0010" else '0';
	AddrRr <= 	CO(9)&CO(3 downto 0);

end PU;
