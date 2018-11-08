entity decoder is port (
    A, B, E: in bit;
    D: out bit_vector(0 to 3));
end decoder;

Architecture DecoderArch of decoder is
begin
    D(0) <= not ((not A) and (not B) and (not E));
    D(1) <= not (not A and B and not E);
    D(2) <= not (A and not B and not E);
    D(3) <= not (A and B and not E);
end DecoderArch;

