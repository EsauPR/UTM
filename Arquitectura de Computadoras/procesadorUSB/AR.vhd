---------------------------------------------------------------------------------------------------
--
-- Title       : AR
-- Design      : UC
-- Author      : POT2
-- Company     : --
--
---------------------------------------------------------------------------------------------------
--
-- File        : AR.vhd
-- Generated   : Wed May 20 10:30:37 2015
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
--{entity {AR} architecture {AR}}

library IEEE;
use IEEE.STD_LOGIC_1164.all;
use IEEE.STD_LOGIC_UNSIGNED.ALL;


entity AR is
	port(
	 clk : in STD_LOGIC;
	 AddrRd : in STD_LOGIC_VECTOR(4 downto 0);
	 AddrRr : in STD_LOGIC_VECTOR(4 downto 0);
	 ctr : in STD_LOGIC;
	 DataIn : in STD_LOGIC_VECTOR(7 downto 0);
	 Rr	: out STD_LOGIC_VECTOR(7 downto 0);
	 Rd : out STD_LOGIC_VECTOR(7 downto 0)
	 
	     );
end AR;

--}} End of automatically maintained section

architecture AR of AR is
type mem is array (31 downto 0) of STD_LOGIC_VECTOR(7 downto 0);
signal AR : mem;
begin

	process (clk)
	begin
		if falling_edge( clk ) then
			if ctr = '1' then
				AR(conv_integer(AddrRd)) <= DataIn;
			end if;
		end if;
	end process;

	Rd <= AR(conv_integer(AddrRd));
	Rr <= AR(conv_integer(AddrRr));

end AR;
