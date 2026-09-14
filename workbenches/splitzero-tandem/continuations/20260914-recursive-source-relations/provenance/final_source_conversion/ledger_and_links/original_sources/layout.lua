local chars = {}
chars["±"] = true
chars["×"] = true
chars["Γ"] = true
chars["Δ"] = true
chars["Θ"] = true
chars["Λ"] = true
chars["Ξ"] = true
chars["Π"] = true
chars["Σ"] = true
chars["Φ"] = true
chars["Ψ"] = true
chars["α"] = true
chars["β"] = true
chars["γ"] = true
chars["δ"] = true
chars["ε"] = true
chars["ζ"] = true
chars["η"] = true
chars["θ"] = true
chars["ι"] = true
chars["κ"] = true
chars["λ"] = true
chars["μ"] = true
chars["ν"] = true
chars["ξ"] = true
chars["π"] = true
chars["ρ"] = true
chars["σ"] = true
chars["τ"] = true
chars["υ"] = true
chars["φ"] = true
chars["χ"] = true
chars["ψ"] = true
chars["ω"] = true
chars["ℓ"] = true
chars["→"] = true
chars["↠"] = true
chars["↦"] = true
chars["∂"] = true
chars["∇"] = true
chars["∏"] = true
chars["−"] = true
chars["∞"] = true
chars["∨"] = true
chars["∩"] = true
chars["∪"] = true
chars["∫"] = true
chars["≃"] = true
chars["≅"] = true
chars["≈"] = true
chars["≠"] = true
chars["≤"] = true
chars["≥"] = true
chars["⊂"] = true
chars["⊆"] = true
chars["⊕"] = true
chars["⊗"] = true
chars["⊣"] = true
chars["⊥"] = true
chars["⋆"] = true
chars["〈"] = true
chars["〉"] = true
chars["𝔢"] = true

local function esc(s)
  return (s:gsub('([#$%%&_{}])','\\%1'):gsub('~','\\textasciitilde{}'):gsub('%^','\\textasciicircum{}'))
end
local function piece(s,code)
  if code or #s>=35 then return '\\protect\\path{'..s..'}' else return esc(s) end
end
local function output(s,code)
  local o={}; local acc={}; local has=false
  for _,v in utf8.codes(s) do
    local c=utf8.char(v)
    if chars[c] then
      has=true
      if #acc>0 then table.insert(o,piece(table.concat(acc),code));acc={} end
      local cm=c
      if c=='〈' then cm='\\langle' end
      if c=='〉' then cm='\\rangle' end
      table.insert(o,'\\allowbreak{}\\ensuremath{'..cm..'}\\allowbreak{}')
    else table.insert(acc,c) end
  end
  if not has and not code and #s<35 then return nil end
  if #acc>0 then table.insert(o,piece(table.concat(acc),code)) end
  return pandoc.RawInline('latex',table.concat(o))
end
function Str(el) return output(el.text,false) end
function Code(el) return output(el.text,true) end
function Math(el)
 if el.mathtype=='DisplayMath' then return pandoc.RawInline('latex','\\LedgerDisplay{'..el.text..'}') end
end
