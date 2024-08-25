from GeradorExperimentos import GeradorExperimentos
from JsonManager import JsonManager

g = GeradorExperimentos(3, 8, 200000)


dctt_alpha_B = g.getAlphaDict(50000, "B", 5)
JsonManager.saveJson(dctt_alpha_B, "alphaMultiCaminhos.json", "alphas")

dctt_beta_B = g.getBetaDict(100000, "B", 10)
JsonManager.saveJson(dctt_beta_B, "betaMultiCaminhos.json", "betas")

dctt_alpha_C = g.getAlphaDict(50000, "C", 5)
JsonManager.saveJson(dctt_alpha_C, "alphaCascata.json", "alphas")

dctt_beta_C = g.getBetaDict(100000, "C", 10)
JsonManager.saveJson(dctt_beta_C, "betaCascata.json", "betas")

dctt_alpha_P = g.getAlphaDict(50000, "P", 5)
JsonManager.saveJson(dctt_alpha_P, "alphaPolifasica.json", "alphas")

dctt_beta_P = g.getBetaDict(100000, "P", 10)
JsonManager.saveJson(dctt_beta_P, "betaPolifasica.json", "betas")