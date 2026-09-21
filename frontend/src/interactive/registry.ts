import type { ComponentType } from "react";
import { PhasePortrait, Resonance, VectorMoment } from "./nm";
import { BeamDiagrams, EulerBuckling, MohrCircle } from "./mq";
import { TensorTransform, YieldSurfaces } from "./tmm";
import { CircularPlate, PlateDeflection, PlateModes } from "./pq";
import { Convergence, FDStability, Isoparametric } from "./su";

/**
 * Mavzu id → interaktiv chizma.
 *
 * Kalitlar haqiqiy mavzu id lari ekani `backend/tests/test_interactive.py`
 * da tekshiriladi, shunda mavzu id i o'zgarsa chizma jimgina yo'qolmaydi.
 */
export const INTERACTIVE: Record<string, { title: string; Component: ComponentType }> = {
  // Nazariy mexanika
  "nm-01": { title: "Vektor moment va yelka", Component: VectorMoment },
  "nm-24": { title: "Mayatnik fazaviy portreti", Component: PhasePortrait },
  "nm-27": { title: "Amplituda-chastota tavsifi", Component: Resonance },
  // Materiallar qarshiligi
  "mq-12": { title: "Q va M epyuralari", Component: BeamDiagrams },
  "mq-19": { title: "Mor doirasi", Component: MohrCircle },
  "mq-25": { title: "Eyler ustuvorligi", Component: EulerBuckling },
  // Tutash muhitlar mexanikasi
  "tmm-02": { title: "Tenzorning burilishi va invariantlar", Component: TensorTransform },
  "tmm-21": { title: "Mizes va Treska yuzalari", Component: YieldSurfaces },
  // Plastinalar va qobiqlar
  "pq-07": { title: "Navye yechimi: egilish sirti", Component: PlateDeflection },
  "pq-13": { title: "Doiraviy plastina: qisilgan va sharnirli", Component: CircularPlate },
  "pq-22": { title: "Tebranish shakllari va tugun chiziqlari", Component: PlateModes },
  // Sonli usullar
  "su-10": { title: "Ayirma sxemasining barqarorligi", Component: FDStability },
  "su-14": { title: "Izoparametrik almashtirish va det J", Component: Isoparametric },
  "su-18": { title: "Yaqinlashish tartibini o'lchash", Component: Convergence },
};

export function interactiveFor(topicId: string) {
  return INTERACTIVE[topicId];
}
